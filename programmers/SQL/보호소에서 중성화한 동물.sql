-- inner join 이용
SELECT OUTS.ANIMAL_ID, OUTS.ANIMAL_TYPE, OUTS.NAME
FROM ANIMAL_OUTS OUTS
JOIN ANIMAL_INS INS 
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE INS.SEX_UPON_INTAKE LIKE '%Intact%' and OUTS.SEX_UPON_OUTCOME NOT LIKE '%Intact%'
ORDER BY OUTS.ANIMAL_ID ASC;



-- 서브쿼리 이용
SELECT ANIMAL_ID, ANIMAL_TYPE, NAME
FROM ANIMAL_OUTS
WHERE ANIMAL_ID IN (
    SELECT ANIMAL_ID
    FROM ANIMAL_INS
    WHERE SEX_UPON_INTAKE IN('Intact Female', 'Intact Male'))
    
AND SEX_UPON_OUTCOME IN('Spayed Female', 'Neutered Male')
ORDER BY ANIMAL_ID