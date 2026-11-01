CREATE TABLE IF NOT EXISTS notification_emails(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
    recipient_id INT,
    subject VARCHAR,
    body TEXT
);

CREATE OR REPLACE FUNCTION trigger_fn_send_email_on_balance_change()
RETURNS TRIGGER
AS
$$
    BEGIN
        INSERT INTO notification_emails(recipient_id, subject, body)
        VALUES (
                new.account_id,
                ('Balance change for account: %', new.acccount_id),
                   'On ' || DATE(NOW) || ' your balance was changed from '|| NEW.old_sum || ' to ' || new.new_sum || '.'
               );
        RETURN new;
        END;
$$
LANGUAGE plpgsql;

CREATE TRIGGER tr_send_email_on_balance_change
    AFTER UPDATE 
    ON logs
    FOR EACH ROW
EXECUTE FUNCTION trigger_fn_send_email_on_balance_change();


