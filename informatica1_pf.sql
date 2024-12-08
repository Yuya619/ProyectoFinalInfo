-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 08-12-2024 a las 20:44:09
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `informatica1_pf`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `diagnosticos`
--

CREATE TABLE `diagnosticos` (
  `ID` int(15) NOT NULL,
  `tipo_imagen` varchar(15) NOT NULL,
  `resultado_IA` text NOT NULL,
  `fecha_imagen` date DEFAULT NULL,
  `fecha_diagnostico` date NOT NULL,
  `estado` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `diagnosticos`
--

INSERT INTO `diagnosticos` (`ID`, `tipo_imagen`, `resultado_IA`, `fecha_imagen`, `fecha_diagnostico`, `estado`) VALUES
(4312, 'mri', '90', '2024-11-15', '2024-11-16', 'revisado'),
(12345, 'mri', 'Tumores: La presencia de masas, ya sean benignas (como meningiomas) o malignas (como gliomas, metástasis), debe ser evaluada en términos de ubicación, bordes, tamaño y características de la imagen (por ejemplo, áreas de necrosis, realce post-contraste)', NULL, '2024-11-15', 'revisado'),
(5684, 'rx', '10', '2024-11-23', '2024-11-26', 'no revisado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pacientes`
--

CREATE TABLE `pacientes` (
  `ID` int(15) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `edad` int(3) NOT NULL,
  `genero` varchar(15) NOT NULL,
  `historial` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pacientes`
--

INSERT INTO `pacientes` (`ID`, `nombre`, `edad`, `genero`, `historial`) VALUES
(4312, 'Peter', 56, 'masculino', 'episodio febril'),
(12345, 'Julieta Maria', 45, 'otros', 'cuerdas vocales inflamadas y gripa'),
(5684, 'juanita', 45, 'femenino', 'hipertensión');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `user_id` int(15) NOT NULL,
  `username` varchar(15) NOT NULL,
  `password` varchar(15) NOT NULL,
  `role` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`user_id`, `username`, `password`, `role`) VALUES
(1028022590, 'yuya_1995', '123456', 'administrador'),
(1098745204, 'jhon_zp', '1234576', 'tecnico'),
(39299344, 'oma_1495', '1234576', 'medico'),
(4321, 'raul', '654321', 'medico'),
(9876, 'adrian', '67890', 'administrador'),
(104350, 'Esteban', '4321', 'tecnico');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
