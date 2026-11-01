CREATE OR REPLACE PROCEDURE sp_transfer_money(
    sender_id INT,
    receiver_id INT,
    amount NUMERIC(19,4)
)
AS
$$
    DECLARE
        current_amount NUMERIC(19,4);
    BEGIN
        current_amount := (SELECT accounts.balance from accounts WHERE id = sender_id);
        CALL sp_withdraw_money(sender_id, amount);
        IF (current_amount - amount) >= 0 THEN
            CALL sp_deposit_money(receiver_id, amount);
        END IF;
    END;
$$
LANGUAGE plpgsql;

CALL sp_transfer_money(1,5,6000);

SELECT
    balance,
    accounts.id
FROM accounts
WHERE id in (1,5)