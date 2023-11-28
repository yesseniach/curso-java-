CREATE TABLE `demo1`.`customers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `nif` VARCHAR(9) NULL,
  `edad` INT NULL,
  `salary` DECIMAL(14,2) NULL,
  `activo` TINYINT(1) NULL,
  `birthdate` DATE NULL,
  `biography` TEXT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `nif_UNIQUE` (`nif` ASC) VISIBLE);