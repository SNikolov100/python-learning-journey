UPDATE cars
SET condition = 'C'
WHERE (mileage IS NULL OR mileage >= 800000)
        AND
    year <= 2010
        AND
    make <> 'Mercedes-Benz';