CREATE OR REPLACE FUNCTION fn_cash_in_users_games(game_name VARCHAR(50))
RETURNS TABLE(total_cash NUMERIC)
AS
$$
    BEGIN
        RETURN QUERY
            SELECT
                ROUND(SUM( CASE
                         WHEN rw % 2 = 1 THEN cash
                         ELSE 0
                    END ), 2)
            FROM (
                     SELECT
                         ug.cash,
                         ROW_NUMBER() OVER(ORDER BY ug.cash DESC ) AS rw
                     FROM users_games AS ug
                              JOIN games AS g
                                   ON g.id = ug.game_id
                     WHERE g.name = game_name) AS t;

    END;
$$
LANGUAGE plpgsql;

SELECT fn_cash_in_users_games('Delphinium Pacific Giant');



SELECT
    SUM( CASE
            WHEN rw % 2 = 1 THEN cash
            ELSE 0
        END )
    FROM (
        SELECT
            ug.cash,
            ROW_NUMBER() OVER(ORDER BY ug.cash DESC ) AS rw
        FROM users_games AS ug
        JOIN games AS g
        ON g.id = ug.game_id
        WHERE g.name = 'Love in a mist') t;

