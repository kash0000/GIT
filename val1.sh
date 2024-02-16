#!/bin/bash

REG_LOGIN="your_database_login_info"  # replace with your actual database login info

while read sum_count sum_period_end_balance sum_average_cr_balance sum_ledger_balance; do
    echo "Count: $sum_count"
    echo "Period End Balance: $sum_period_end_balance"
    echo "Average CR Balance: $sum_average_cr_balance"
    echo "Ledger Balance: $sum_ledger_balance"
done < <(sqlplus -s $REG_LOGIN<<EOF_SQL
set pagesize 0
set trim on
set head off
set feedback off
set linesize 1000
set echo off
whenever sqlerror exit 1
select count(*),sum(period_end_balance),sum(average_cr_balance),sum(ledger_balance) from BOE_AXIOM_DATA.boe_er partition(Psep);
exit;
EOF_SQL
)
