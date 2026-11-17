SELECT a.username, COALESCE(b.username, 'organic') AS referrer_name
    FROM user_referrals as a
    LEFT JOIN user_referrals as b
    ON  a.referred_by = b.id 
    ORDER BY a.username ASC NULLS LAST