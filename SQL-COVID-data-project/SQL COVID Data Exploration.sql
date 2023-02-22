-- COVID Data Exploration
-- NOTE: This data is outdated; it ends around May 2021.

USE COVIDPortfolioProject

SELECT location, date, total_cases, new_cases, total_deaths, population
FROM COVIDPortfolioProject..CovidDeaths
WHERE continent IS NOT NULL
ORDER BY location, date

-- Looking at Total Cases vs. Total Deaths
-- Suggests likelihood of death if you contract COVID in a specific location at a specific point in time

SELECT location, date, total_cases, total_deaths, (total_deaths / total_cases * 100) AS DeathPercentage
FROM COVIDPortfolioProject..CovidDeaths
WHERE continent IS NOT NULL
ORDER BY location, date

-- Looking at Total Cases vs. Population
-- Percentage of population that was reported to contract COVID

SELECT location, date, total_cases, population, (total_cases / population * 100) AS CasePercentage
FROM COVIDPortfolioProject..CovidDeaths
WHERE continent IS NOT NULL
ORDER BY location, date

-- Looking at Total Deaths vs. Population
-- Suggests likelihood of death in a specific location

SELECT location, date, total_deaths, population, (total_deaths / population * 100) AS DeathPercentageOfPopulation
FROM COVIDPortfolioProject..CovidDeaths
WHERE continent IS NOT NULL
ORDER BY location, date

-- Looking at Countries with Highest Infection Rate compared to Population

SELECT location, population, MAX(total_cases) AS HighestCaseCount, (MAX(total_cases) / population * 100) AS PercentPopulationInfected
FROM COVIDPortfolioProject..CovidDeaths
WHERE continent IS NOT NULL
GROUP BY location, population
ORDER BY PercentPopulationInfected DESC

-- Looking at Countries with Highest Deaths
-- By the way, here we use CAST(total_deaths AS BIGINT) because the data is an nvarchar.

SELECT location, MAX(CAST(total_deaths as bigint)) AS TotalDeathCount
FROM COVIDPortfolioProject..CovidDeaths
WHERE continent IS NOT NULL
GROUP BY location
ORDER BY TotalDeathCount DESC

-- How about total deaths by continent?

SELECT location, MAX(CAST(total_deaths AS BIGINT)) AS TotalDeathCount
FROM COVIDPortfolioProject..CovidDeaths
WHERE continent IS NULL
GROUP BY location
ORDER BY TotalDeathCount DESC

-- OR:

SELECT continent, SUM(CAST(total_deaths AS BIGINT)) AS TotalDeathCount
FROM COVIDPortfolioProject..CovidDeaths
WHERE continent IS NOT NULL
AND date = '2021-04-30 00:00:00.000'
GROUP BY continent
ORDER BY TotalDeathCount DESC

-- This dataset already has global statistics under location = 'World', but let's figure those out on our own anyway,
-- just to show I can.

SELECT SUM(new_cases) AS TotalCases, SUM(CAST(new_deaths AS BIGINT)) AS TotalDeaths, (SUM(CAST(new_deaths AS BIGINT)) / SUM(new_cases) * 100) AS DeathsAsPercentageOfCases
FROM COVIDPortfolioProject..CovidDeaths
WHERE continent IS NOT NULL

-- We can also look at this by date:

SELECT date, SUM(new_cases) AS TotalCases, SUM(CAST(new_deaths AS BIGINT)) AS TotalDeaths, (SUM(CAST(new_deaths AS BIGINT)) / SUM(new_cases) * 100) AS DeathsAsPercentageOfCases
FROM COVIDPortfolioProject..CovidDeaths
WHERE continent IS NOT NULL
GROUP BY date
ORDER BY date

-- All of that was just using our CovidDeaths table. We also have the CovidVaccinations table.

SELECT *
FROM COVIDPortfolioProject..CovidVaccinations

-- Let's join these two tables!

SELECT *
FROM COVIDPortfolioProject..CovidDeaths AS d
JOIN COVIDPortfolioProject..CovidVaccinations AS v
ON d.location = v.location AND d.date = v.date

-- Looking at Total Population vs. New Vaccinations

SELECT d.continent, d.location, d.date, d.population, v.new_vaccinations
FROM COVIDPortfolioProject..CovidDeaths AS d
JOIN COVIDPortfolioProject..CovidVaccinations AS v
ON d.location = v.location AND d.date = v.date
WHERE d.continent IS NOT NULL
ORDER BY d.location, d.date

-- Using a Partition By to get Total Vaccinations

SELECT d.continent, d.location, d.date, d.population, v.new_vaccinations,
SUM(CAST(v.new_vaccinations AS BIGINT)) OVER (PARTITION BY d.location ORDER BY d.location, d.date) AS TotalVaccinationsByDate
FROM COVIDPortfolioProject..CovidDeaths AS d
JOIN COVIDPortfolioProject..CovidVaccinations AS v
ON d.location = v.location AND d.date = v.date
WHERE d.continent IS NOT NULL
ORDER BY d.location, d.date

-- Next, we'll use this previous query to make a CTE to investigate further and look at TotalVaccinationsByDate as a percentage of Population.

WITH PopulationVsRollingVaccinations (continent, location, date, population, new_vaccinations, TotalVaccinationsByDate)
AS (
SELECT d.continent, d.location, d.date, d.population, v.new_vaccinations,
SUM(CAST(v.new_vaccinations AS BIGINT)) OVER (PARTITION BY d.location ORDER BY d.location, d.date) AS TotalVaccinationsByDate
FROM COVIDPortfolioProject..CovidDeaths AS d
JOIN COVIDPortfolioProject..CovidVaccinations AS v
ON d.location = v.location AND d.date = v.date
WHERE d.continent IS NOT NULL
)
SELECT continent, location, date, population, new_vaccinations, TotalVaccinationsByDate,
(TotalVaccinationsByDate / population * 100) AS TotalVaxByDatePercentage
FROM PopulationVsRollingVaccinations

-- We could also use a temp table instead if we really wanted to:

DROP TABLE IF EXISTS #PercentPopVaccinated
CREATE TABLE #PercentPopVaccinated (
continent nvarchar(255),
location nvarchar(255), 
date datetime,
population numeric,
new_vaccinations numeric,
TotalVaccinationsByDate numeric
)

INSERT INTO #PercentPopVaccinated
SELECT d.continent, d.location, d.date, d.population, v.new_vaccinations,
SUM(CAST(v.new_vaccinations AS BIGINT)) OVER (PARTITION BY d.location ORDER BY d.location, d.date) AS TotalVaccinationsByDate
FROM COVIDPortfolioProject..CovidDeaths AS d
JOIN COVIDPortfolioProject..CovidVaccinations AS v
ON d.location = v.location AND d.date = v.date
WHERE d.continent IS NOT NULL

SELECT continent, location, date, population, new_vaccinations, TotalVaccinationsByDate,
(TotalVaccinationsByDate / population * 100) AS TotalVaxByDatePercentage
FROM #PercentPopVaccinated
ORDER BY location, date

-- There's more data besides just deaths and vaccinations. We also have testing data.
-- This can allow us to draw conclusions about the testing regimes of particular countries.
-- For instance, we don't have any data about testing in Afghanistan.

SELECT continent, location, date, new_tests, total_tests, positive_rate
FROM COVIDPortfolioProject..CovidVaccinations
WHERE continent IS NOT NULL
ORDER BY location, date

-- The following query tells us the highest number of tests conducted in one day, total tests conducted, and highest
-- positive test rate in a given country.

SELECT continent, location, population, MAX(new_tests) AS HighestTestsPerDay, MAX(total_tests) AS TotalTests, MAX(positive_rate) AS HighestPositiveRate
FROM COVIDPortfolioProject..CovidVaccinations
WHERE continent IS NOT NULL
GROUP BY location, continent, population
ORDER BY HighestPositiveRate DESC

-- We could conclude that Bosnia and Herzegovina could have had a really nasty period of high COVID infections, 
-- but we could also notice that its testing regime was relatively weak.
-- Bhutan had a really low maximum positive rate (0.012%), but is that due to its abysmal testing regime
-- (under 10k tests by May 2021?) or perhaps a large number of isolated mountain communities?
-- Check out South Korea: its testing regime seems pretty robust, and may have had an unusually good
-- program for avoiding infections, with its high population (51m) and low positive rates (0.049% at highest).

-- Let's create some views for visualizations.

CREATE VIEW TotalVaccinationsByDate AS 
SELECT d.continent, d.location, d.date, d.population, v.new_vaccinations,
SUM(CAST(v.new_vaccinations AS BIGINT)) OVER (PARTITION BY d.location ORDER BY d.location, d.date) AS TotalVaccinationsByDate
FROM COVIDPortfolioProject..CovidDeaths AS d
JOIN COVIDPortfolioProject..CovidVaccinations AS v
ON d.location = v.location AND d.date = v.date
WHERE d.continent IS NOT NULL

CREATE VIEW PercentPopulationInfected AS
SELECT location, population, MAX(total_cases) AS HighestCaseCount, (MAX(total_cases) / population * 100) AS PercentPopulationInfected
FROM COVIDPortfolioProject..CovidDeaths
WHERE continent IS NOT NULL
GROUP BY location, population

CREATE VIEW DeathsByCountry AS
SELECT location, MAX(CAST(total_deaths as bigint)) AS TotalDeathCount
FROM COVIDPortfolioProject..CovidDeaths
WHERE continent IS NOT NULL
GROUP BY location

CREATE VIEW TestingRegimeData AS
SELECT continent, location, population, MAX(new_tests) AS HighestTestsPerDay, MAX(total_tests) AS TotalTests, MAX(positive_rate) AS HighestPositiveRate
FROM COVIDPortfolioProject..CovidVaccinations
WHERE continent IS NOT NULL
GROUP BY location, continent, population