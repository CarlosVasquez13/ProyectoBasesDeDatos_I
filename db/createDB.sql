-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema Sudoku
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Sudoku
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Sudoku` DEFAULT CHARACTER SET utf8 ;
USE `Sudoku` ;

-- -----------------------------------------------------
-- Table `Sudoku`.`Usuario_Tipo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Sudoku`.`Usuario_Tipo` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `fecha` TIMESTAMP DEFAULT NOW(),
  `activo` TIMESTAMP DEFAULT NOW() ON UPDATE NOW(),
  `modificado` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Sudoku`.`Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Sudoku`.`Usuario` (
  `Id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NULL,
  `clave` VARCHAR(45) NOT NULL,
  `nombre_usuario` VARCHAR(45) NOT NULL,
  `creado` TIMESTAMP DEFAULT NOW(),
  `modficado` TIMESTAMP DEFAULT NOW() ON UPDATE NOW(),
  `activo` TINYINT(1) NOT NULL DEFAULT 1,
  `usuarioTipo_id` INT NOT NULL,
  PRIMARY KEY (`Id`),
  INDEX `fk_Usuarios_UsuarioTipo_idx` (`usuarioTipo_id` ASC),
  CONSTRAINT `fk_Usuarios_UsuarioTipo`
    FOREIGN KEY (`usuarioTipo_id`)
    REFERENCES `Sudoku`.`Usuario_Tipo` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Sudoku`.`Tablero`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Sudoku`.`Tablero` (
  `id` INT NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `creado` TIMESTAMP DEFAULT NOW(),
  `activo` TINYINT(1) NULL DEFAULT 1,
  `modificado` TIMESTAMP DEFAULT NOW() ON UPDATE NOW(),
  `descripcion` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Sudoku`.`TableroTIpo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Sudoku`.`TableroTIpo` (
  `idTablero` INT NOT NULL,
  `Nombre` VARCHAR(45) NULL,
  `Creado` TIMESTAMP DEFAULT NOW(),
  `Modificado` TIMESTAMP DEFAULT NOW() ON UPDATE NOW(),
  `Activo` TINYINT(1) NULL,
  PRIMARY KEY (`idTablero`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Sudoku`.`TableroDetalle`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Sudoku`.`TableroDetalle` (
  `id` INT NOT NULL,
  `tablero_id` INT NOT NULL,
  `fila` INT NULL,
  `valor` VARCHAR(45) NULL,
  `posicion_x` VARCHAR(45) NOT NULL,
  `posicion_y` VARCHAR(45) NOT NULL,
  `fecha` TIMESTAMP DEFAULT NOW(),
  `modificado` TIMESTAMP DEFAULT NOW() ON UPDATE NOW(),
  `activo` TINYINT(1) NULL DEFAULT 1,
  PRIMARY KEY (`id`),
  INDEX `fk_TableroDetalle_Tablero1_idx` (`tablero_id` ASC),
  CONSTRAINT `fk_TableroDetalle_Tablero1`
    FOREIGN KEY (`tablero_id`)
    REFERENCES `Sudoku`.`Tablero` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Sudoku`.`Juegos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Sudoku`.`Juego` (
  `id` INT NOT NULL ,
  `usuario_id` INT NOT NULL,
  `estado` VARCHAR(20) NULL,
  `tablero_id` INT NOT NULL,
  `fecha_inicio` TIMESTAMP DEFAULT NOW(),
  `fecha_finalizado` DATETIME NULL,
  `abandono` TINYINT(1) NULL DEFAULT 0,
  PRIMARY KEY (`id`),
  INDEX `fk_HistorialJuegos_Usuarios1_idx` (`usuario_id` ASC),
  INDEX `fk_Juegos_Tablero1_idx` (`tablero_id` ASC),
  CONSTRAINT `fk_HistorialJuegos_Usuarios1`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `Sudoku`.`Usuario` (`Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Juegos_Tablero1`
    FOREIGN KEY (`tablero_id`)
    REFERENCES `Sudoku`.`Tablero` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Sudoku`.`Jugadas_Historial`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Sudoku`.`Jugadas_Historial` (
  `id` INT NOT NULL,
  `dato` VARCHAR(45) NOT NULL,
  `x` INT NOT NULL,
  `y` INT NOT NULL,
  `Juego_id` INT NOT NULL,
	`fecha` TIMESTAMP DEFAULT NOW(),
  PRIMARY KEY (`id`),
  INDEX `fk_Jugadas_Juegos1_idx` (`Juego_id` ASC),
  CONSTRAINT `fk_Jugadas_Juegos1`
    FOREIGN KEY (`Juego_id`)
    REFERENCES `Sudoku`.`Juegos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Sudoku`.`Accion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Sudoku`.`Accion` (
  `id` INT NOT NULL,
  `nombre` VARCHAR(45) NULL,
  `descripcion` VARCHAR(45) NULL,
  `creado` TIMESTAMP DEFAULT NOW(),
  `modificado` TIMESTAMP DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Sudoku`.`Bitacora`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Sudoku`.`Bitacora` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `creado` TIMESTAMP DEFAULT NOW(),
  `esJugada` TINYINT(1) NULL DEFAULT 0,
  `jugada_Id` INT NULL,
  `usuario_id` INT NOT NULL,
  `accion_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Bitacora_Usuarios1_idx` (`usuario_id` ASC),
  INDEX `fk_Bitacora_Acciones1_idx` (`accion_id` ASC),
  CONSTRAINT `fk_Bitacora_Usuarios1`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `Sudoku`.`Usuario` (`Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Bitacora_Acciones1`
    FOREIGN KEY (`accion_id`)
    REFERENCES `Sudoku`.`Accion` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
