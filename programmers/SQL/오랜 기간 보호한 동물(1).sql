-- 코드를 입력하세요
SELECT AINS.NAME, AINS.DATETIME
FROM ANIMAL_INS AINS
LEFT JOIN ANIMAL_OUTS AOUTS 
ON AOUTS.ANIMAL_ID = AINS.ANIMAL_ID
WHERE AOUTS.ANIMAL_ID IS NULL
ORDER BY AINS.DATETIME 
LIMIT 3

-- https://yoo-hyeok.tistory.com/98 참고해보기 (1006에 읽어보기)