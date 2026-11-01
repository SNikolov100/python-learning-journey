import random
from decimal import Decimal
from datetime import datetime, timedelta

from django.core.exceptions import ValidationError
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    MinLengthValidator,
    MaxLengthValidator,
)
from django.db import IntegrityError
from django.db.models import (
    AutoField,
    BigAutoField,
    PositiveIntegerField,
    PositiveSmallIntegerField,
    BooleanField,
    CharField,
    TextField,
    EmailField,
    DecimalField,
    DateField,
    DateTimeField,
    IntegerField,
    SmallIntegerField,
    BigIntegerField,
)
from django.db.models.fields.related import ForeignKey, OneToOneField
from django.utils import timezone


def get_validator_limit(validator):
    """
    Returns validator.limit_value.
    If limit_value is callable, calls it.
    """
    limit_value = validator.limit_value

    if callable(limit_value):
        return limit_value()

    return limit_value


def get_min_value(field, default=None):
    """
    Reads MinValueValidator from field.validators.
    """
    min_value = default

    for validator in field.validators:
        if isinstance(validator, MinValueValidator):
            value = get_validator_limit(validator)

            if min_value is None or value > min_value:
                min_value = value

    return min_value


def get_max_value(field, default=None):
    """
    Reads MaxValueValidator from field.validators.
    """
    max_value = default

    for validator in field.validators:
        if isinstance(validator, MaxValueValidator):
            value = get_validator_limit(validator)

            if max_value is None or value < max_value:
                max_value = value

    return max_value


def get_min_length(field, default=1):
    """
    Reads MinLengthValidator from field.validators.
    """
    min_length = default

    for validator in field.validators:
        if isinstance(validator, MinLengthValidator):
            value = get_validator_limit(validator)

            if value > min_length:
                min_length = value

    return min_length


def get_max_length(field):
    """
    Uses field.max_length and MaxLengthValidator if available.
    """
    max_length = getattr(field, "max_length", None)

    for validator in field.validators:
        if isinstance(validator, MaxLengthValidator):
            value = get_validator_limit(validator)

            if max_length is None or value < max_length:
                max_length = value

    return max_length


def generate_integer_value(field):
    """
    Generates integer values according to MinValueValidator and MaxValueValidator.
    """
    if isinstance(field, (PositiveIntegerField, PositiveSmallIntegerField)):
        default_min = 0
    else:
        default_min = -100

    default_max = 100

    min_value = get_min_value(field, default=default_min)
    max_value = get_max_value(field, default=default_max)

    min_value = int(min_value)
    max_value = int(max_value)

    if min_value > max_value:
        min_value, max_value = max_value, min_value

    return random.randint(min_value, max_value)


def generate_decimal_value(field):
    """
    Generates Decimal values according to:
    - max_digits
    - decimal_places
    - MinValueValidator
    - MaxValueValidator
    """
    decimal_places = field.decimal_places
    max_digits = field.max_digits

    max_whole_digits = max_digits - decimal_places

    largest_possible = (
        Decimal(10) ** max_whole_digits
    ) - (Decimal(1) / (Decimal(10) ** decimal_places))

    smallest_possible = Decimal("0")

    min_value = get_min_value(field, default=smallest_possible)
    max_value = get_max_value(field, default=largest_possible)

    min_value = Decimal(str(min_value))
    max_value = Decimal(str(max_value))

    if min_value > max_value:
        min_value, max_value = max_value, min_value

    random_float = random.uniform(float(min_value), float(max_value))

    return Decimal(str(random_float)).quantize(
        Decimal("1") / (Decimal(10) ** decimal_places)
    )


def generate_string_value(field, model, created, attempts):
    """
    Generates valid text for CharField, TextField and EmailField.
    Respects MinLengthValidator, MaxLengthValidator and max_length.
    """
    min_length = get_min_length(field, default=1)
    max_length = get_max_length(field)

    if isinstance(field, EmailField):
        value = f"user{created + 1}_{attempts}@example.com"

        if max_length and len(value) > max_length:
            value = f"u{created + 1}@x.com"

        return value

    base_value = f"{model.__name__}_{field.name}_{created + 1}_{attempts}"

    if len(base_value) < min_length:
        base_value = base_value + ("x" * (min_length - len(base_value)))

    if max_length and len(base_value) > max_length:
        base_value = base_value[:max_length]

        if len(base_value) < min_length:
            base_value = base_value.ljust(min_length, "x")

    return base_value


def generate_date_value():
    """
    Generates random date.
    """
    start_date = datetime(2000, 1, 1).date()
    end_date = timezone.now().date()

    delta = end_date - start_date
    random_days = random.randint(0, delta.days)

    return start_date + timedelta(days=random_days)


def generate_datetime_value():
    """
    Generates timezone-aware datetime.
    """
    start_datetime = timezone.now() - timedelta(days=3650)
    end_datetime = timezone.now()

    delta_seconds = int((end_datetime - start_datetime).total_seconds())
    random_seconds = random.randint(0, delta_seconds)

    return start_datetime + timedelta(seconds=random_seconds)


def generate_field_value(field, model, created, attempts):
    """
    Generates value according to field type.
    """

    # Choices must be checked early
    if getattr(field, "choices", None):
        return random.choice(field.choices)[0]

    if isinstance(field, BooleanField):
        return random.choice([True, False])

    if isinstance(
        field,
        (
            PositiveIntegerField,
            PositiveSmallIntegerField,
            IntegerField,
            SmallIntegerField,
            BigIntegerField,
        ),
    ):
        return generate_integer_value(field)

    if isinstance(field, DecimalField):
        return generate_decimal_value(field)

    if isinstance(field, (CharField, TextField, EmailField)):
        return generate_string_value(field, model, created, attempts)

    if isinstance(field, DateTimeField):
        return generate_datetime_value()

    if isinstance(field, DateField):
        return generate_date_value()

    if isinstance(field, (ForeignKey, OneToOneField)):
        related_model = field.related_model

        related_instance = related_model.objects.order_by("?").first()

        if related_instance:
            return related_instance

        if field.null:
            return None

        raise ValueError(
            f"Cannot populate {model.__name__}.{field.name}. "
            f"The related model {related_model.__name__} has no records."
        )

    return None


def populate_model_with_data(model, num_records=10, max_attempts=1000):
    """
    Populates a Django model with random valid data.

    Important:
    - Calls full_clean() before save()
    - Respects Django validators as much as possible
    - Does not stop on ValidationError
    - Avoids infinite loops with max_attempts
    - Handles ManyToMany fields after save()
    """

    model_fields = model._meta.fields
    many_to_many_fields = model._meta.local_many_to_many

    created = 0
    attempts = 0

    while created < num_records and attempts < max_attempts:
        attempts += 1
        field_values = {}

        try:
            for field in model_fields:

                # Skip primary keys
                if isinstance(field, (AutoField, BigAutoField)):
                    continue

                # Skip auto fields like auto_now and auto_now_add
                if getattr(field, "auto_now", False):
                    continue

                if getattr(field, "auto_now_add", False):
                    continue

                value = generate_field_value(
                    field=field,
                    model=model,
                    created=created,
                    attempts=attempts,
                )

                if value is not None or field.null:
                    field_values[field.name] = value

            instance = model(**field_values)

            # This is the important validation step
            instance.full_clean()

            instance.save()

            # Handle ManyToMany fields after instance is saved
            for field in many_to_many_fields:
                related_model = field.related_model

                related_count = related_model.objects.count()

                if related_count == 0:
                    continue

                number_of_items = random.randint(
                    1,
                    min(5, related_count)
                )

                related_instances = related_model.objects.order_by("?")[
                    :number_of_items
                ]

                getattr(instance, field.name).set(related_instances)

            created += 1

        except ValidationError as error:
            print(
                f"ValidationError skipped for {model.__name__}: {error}"
            )
            continue

        except IntegrityError as error:
            print(
                f"IntegrityError skipped for {model.__name__}: {error}"
            )
            continue

        except ValueError as error:
            print(error)
            break

    print(
        f"{model.__name__}: created {created}/{num_records} records "
        f"after {attempts} attempts."
    )