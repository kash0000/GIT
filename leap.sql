DECLARE
    v_date DATE := TO_DATE('30-Apr-2024', 'DD-MON-YYYY'); -- Example date
    v_leap_year NUMBER;
    days_in_year NUMBER;
BEGIN
    -- Determine if the year is a leap year
    SELECT COUNT(*)
    INTO v_leap_year
    FROM DUAL
    WHERE TO_NUMBER(TO_CHAR(v_date, 'YYYY')) = EXTRACT(YEAR FROM ADD_MONTHS(LAST_DAY(v_date), 2));

    -- Use a case statement to determine the number of days in the year
    days_in_year := CASE
                        WHEN v_leap_year = 1 THEN 366 -- Leap year has 366 days
                        ELSE 365    -- Non-leap year has 365 days
                    END;

    -- Print the value of the variable
    DBMS_OUTPUT.PUT_LINE('Days in year: ' || days_in_year);
END;
/
