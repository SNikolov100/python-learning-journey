CREATE OR REPLACE PROCEDURE sp_players_team_name(
    IN player_name VARCHAR(50),
    OUt team_name VARCHAR(45))
AS
$$
    BEGIN
        SELECT
            t.name
        INTO team_name
        FROM teams AS t
                 JOIN players AS p
                      ON p.team_id = t.id
        WHERE CONCAT(p.first_name, ' ', p.last_name) = player_name;
        IF team_name IS NULL THEN team_name := 'The player currently has no team';
        end if;
    END;

$$
LANGUAGE plpgsql;


CALL sp_players_team_name('Thor Serrels', '');
CALL sp_players_team_name('Walther Olenchenko', '');

SELECT
    t.name
FROM teams AS t
JOIN players AS p
ON p.team_id = t.id
WHERE CONCAT(p.first_name, ' ', p.last_name) = 'Walther Olenchenko';