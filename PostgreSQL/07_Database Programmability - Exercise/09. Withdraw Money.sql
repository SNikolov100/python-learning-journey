CREATE OR REPLACE PROCEDURE sp_withdraw_money(
    account_id INT,
    money_amount NUMERIC(19,4)
)
AS
$$
    DECLARE
        current_balance NUMERIC(19,4);
    BEGIN
        current_balance := (SELECT balance FROM accounts WHERE id = account_id);
        IF (current_balance - money_amount) < 0 THEN
            RAISE NOTICE 'Insufficient balance to withdraw %', money_amount;
            RETURN ;
        END IF;
        UPDATE accounts
        SET balance = balance - money_amount
        WHERE id = account_id;

    END;
$$
LANGUAGE plpgsql;

SELECT
    id,
    balance
FROM accounts
WHERE id in (1,5,6);

Call sp_withdraw_money(1, 6000);