-- SQLite
-- desc tables;

/*CREATE TABLE Employees (
    EmployeeID INTEGER PRIMARY KEY,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    BirthDate DATE,
    HireDate DATE,
    Position TEXT,
    Salary REAL -- 소수점 타입
);

INSERT INTO Employees
(FirstName, LastName, BirthDate, HireDate, Position, Salary )
VALUES  
('홍', '길동', '1985-03-15', '2010-06-01', '매니저', 60000),
('김', '철수', '1990-07-22', '2015-09-15', '개발자', 55000),
('이', '영희', '1988-11-30', '2012-04-20', '디자이너', 50000),
('박', '민수', '1992-05-10', '2018-01-05', '마케터', 48000),
('최', '수진', '1987-12-25', '2011-03-12', '영업사원', 52000);*/

select * from Employees;

-- Employees table with sample data 한글로 해줘
/*INSERT INTO Employees
(FirstName, LastName, BirthDate, HireDate, Position, Salary )
VALUES  
('김', '철수', '1990-07-22', '2015-09-15', '개발자', 65000);*/

-- SELECT * FROM Employees ORDER BY EmployeeID ASC LIMIT 5 OFFSET (2-1)*5;

-- SELECT * FROM Employees WHERE Salary BETWEEN 60000 AND 80000;

-- IN 절을 사용하여 여러 값 중 하나와 일치하는 데이터 조회
-- SELECT * FROM Employees WHERE Position IN ('개발자', '디자이너');

-- 위와 동일한 쿼리임
-- SELECT * FROM Employees WHERE Position='개발자' OR Position='디자이너';

-- SELECT Position, LastName from Employees;

-- group by 절을 사용하여 그룹화된 데이터 조회
-- SELECT Position, AVG(Salary) AS AverageSalary FROM Employees GROUP BY Position;

-- SELECT Position, SUM(Salary) AS TotalSalary FROM Employees GROUP BY Position;

UPDATE Employees SET Salary = Salary * 1.1 WHERE Position = '개발자';     

SELECT * FROM Employees;