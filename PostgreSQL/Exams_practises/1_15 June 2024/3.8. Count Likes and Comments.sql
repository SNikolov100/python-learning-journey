SELECT
    p.id AS photo_id,
    (SELECT COUNT(*) FROM likes AS l WHERE p.id = l.photo_id) AS likes_count,
    (SELECT COUNT(*) FROM comments AS c WHERE p.id = c.photo_id) AS comments_count
FROM photos AS p
ORDER BY likes_count DESC ,
         comments_count DESC ,
         photo_id
