DECLARE
    v_date DATE := TO_DATE('30-Apr-2024', 'DD-MON-YYYY'); -- Example date
    days_in_year NUMBER;
    v_year NUMBER;
BEGIN
    -- Extract the year from the date
    v_year := TO_NUMBER(TO_CHAR(v_date, 'YYYY'));

    -- Determine if the year is a leap year
    IF (MOD(v_year, 4) = 0 AND MOD(v_year, 100) != 0) OR (MOD(v_year, 400) = 0) THEN
        -- Leap year has 366 days
        days_in_year := 366;
    ELSE
        -- Non-leap year has 365 days
        days_in_year := 365;
    END IF;

    -- Print the value of the variable
    DBMS_OUTPUT.PUT_LINE('Days in year: ' || days_in_year);
END;
/
