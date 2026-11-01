CREATE OR REPLACE FUNCTION fn_is_word_comprised(
    set_of_letters VARCHAR(50),
    word VARCHAR(50)
)
RETURNS BOOLEAN
AS
$$
    BEGIN
        --RETURN TRIM(lower(word), lower(set_of_letters)) = '';
        IF TRIM(lower(word), lower(set_of_letters)) = '' then
            RETURN TRUE;
        else return False;
        END if;
    END;
$$
LANGUAGE plpgsql;

select fn_is_word_comprised('ois tmiah%f', 'halves');

SELECT fn_is_word_comprised('ois tmiah%f', 'Sofia')