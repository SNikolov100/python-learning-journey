CREATE OR REPLACE FUNCTION fn_difficulty_level(level INT)
RETURNS VARCHAR(20)
AS
$$
    BEGIN
        IF level <= 40 THEN RETURN 'Normal Difficulty';
        ELSIF level <= 60 THEN RETURN 'Nightmare Difficulty';
        ELSE RETURN 'Hell Difficulty';
        END IF;
    END;
$$
LANGUAGE plpgsql;

SELECT
    ug.user_id,
    ug.level,
    ug.cash,
    fn_difficulty_level(ug.level)
FROM users_games AS ug
ORDER BY ug.user_id;