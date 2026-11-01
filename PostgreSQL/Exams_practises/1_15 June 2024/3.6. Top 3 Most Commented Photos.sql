SELECT
    p.id AS photo_id,
    p.capture_date,
    p.description,
    count(c.content) AS comments_count
FROM photos AS p
JOIN comments AS c
ON c.photo_id = p.id
WHERE p.description IS NOT NULL
GROUP BY p.id, p.capture_date, p.description
ORDER BY
    comments_count DESC,
    photo_id
LIMIT 3;
