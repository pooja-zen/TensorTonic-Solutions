-- Returns: account, txn_date, amount, running_total.
SELECT account, txn_date, amount, SUM(amount) OVER (PARTITION BY account ORDER BY txn_date ASC, id ASC) AS running_total
    FROM transactions
    --GROUP BY account, txn_date, amount
    ORDER BY account ASC, txn_date ASC , id ASC