CREATE OR REPLACE FUNCTION fn_calculate_future_value(
    initial_sum DECIMAL,
    yearly_interest_rate DECIMAL,
    number_of_years INT
)
RETURNS NUMERIC
AS
$$
    BEGIN
        RETURN trunc(initial_sum * (power((1+yearly_interest_rate), number_of_years)), 4);
    END;
$$
LANGUAGE plpgsql;

select fn_calculate_future_value (1000, 0.1, 5);
select fn_calculate_future_value(500, 0.25, 10);