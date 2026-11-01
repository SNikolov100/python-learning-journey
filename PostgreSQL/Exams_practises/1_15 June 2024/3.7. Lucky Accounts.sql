SELECT
    CONCAT(p.id, ' ',a.username ) AS id_username,
    a.email

FROM photos AS p
         JOIN accounts_photos AS ap
              ON p.id = ap.photo_id
         JOIN accounts AS a
              ON a.id = ap.account_id
WHERE p.id = a.id
ORDER BY ap.account_id