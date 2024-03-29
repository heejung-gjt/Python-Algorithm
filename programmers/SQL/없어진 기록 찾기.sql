-- 천재지변으로 인해 일부 데이터가 유실되었습니다. 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID 순으로 조회하는 SQL문을 작성해주세요.

-- ANIMAL_OUTS 테이블의 ANIMAL_ID는 ANIMAL_INS의 ANIMAL_ID의 외래 키입니다.

-- ANIMAL_INS
-- ANIMAL_ID	ANIMAL_TYPE	  DATETIME	             INTAKE_CONDITION	NAME	SEX_UPON_INTAKE
-- A352713	    Cat	          2017-04-13 16:29:00	 Normal	            Gia	    Spayed Female
-- A350375	    Cat	          2017-03-06 15:01:00	 Normal	            Meo	    Neutered Male
-- ANIMAL_OUTS

-- ANIMAL_OUTS
-- ANIMAL_ID	ANIMAL_TYPE	  DATETIME	            NAME	SEX_UPON_OUTCOME
-- A349733	    Dog	          2017-09-27 19:09:00	Allie	Spayed Female
-- A352713	    Cat	          2017-04-25 12:25:00	Gia	    Spayed Female
-- A349990	    Cat	          2018-02-02 14:18:00	Spice	Spayed Female


SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_OUTS A LEFT JOIN ANIMAL_INS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.ANIMAL_ID IS NULL