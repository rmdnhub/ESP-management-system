-- Base de données : `Enseignants_ESP`
--

-- --------------------------------------------------------

--
-- Structure de la table `duree`
--

CREATE TABLE IF NOT EXISTS `duree` (
  `duree` int(34) NOT NULL,
  PRIMARY KEY (`duree`)
);

-- --------------------------------------------------------

--
-- Structure de la table `em`
--

CREATE TABLE IF NOT EXISTS `em` (
  `code_EM` varchar(11) NOT NULL,
  `nom_EM` varchar(50) DEFAULT NULL,
  `coeff_EM` int(11) DEFAULT NULL,
  `V_CM` float DEFAULT NULL,
  `V_TD` float DEFAULT NULL,
  `V_TP` float DEFAULT NULL,
  PRIMARY KEY (`code_EM`)
);

--
-- Contenu de la table `em`
--

INSERT INTO `em` (`code_EM`, `nom_EM`, `coeff_EM`,`V_CM`, `V_TD`, `V_TP`) VALUES
('IRT21', 'programmation C', 2, 5, 5, 6),
('IRT22', 'programmation Java', 3, 8, 6, 10),
('IRT24', 'réseau informatique', 3, 7, 5, 12),
('IRT25', 'système exploitation', 2, 5, 5, 6);

-- --------------------------------------------------------

--
-- Structure de la table `enseignant`
--

CREATE TABLE IF NOT EXISTS `enseignant` (
  `num_E` int(145) NOT NULL AUTO_INCREMENT,
  `nom_E` varchar(50) DEFAULT NULL,
  `prenom_E` varchar(50) DEFAULT NULL,
  `e_mail_E` varchar(60) DEFAULT NULL,
  `statut_E` varchar(50) DEFAULT NULL,
  `Departement` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`num_E`)
);

--
-- Contenu de la table `enseignant`
--

INSERT INTO `enseignant` (`num_E`, `nom_E`, `prenom_E`, `e_mail_E`, `statut_E`, `Departement`) VALUES
(1, 'louly', 'mohamed aly', 'louly@esp.mr', 'Permanent', 'ST'),
(2, 'hafedh', 'mohamed babou', 'hafedh@esp.mr', 'Permanent', 'IRT'),
(3, 'LAM', 'Mamadou', 'lam@esp.mr', 'Permanent', 'HE'),
(4, 'mohamedou', 'debagh', 'debagh@esp.mr', 'Permanent', 'IRT'),
(5, 'abdallah', 'nasri', 'nasri@esp.mr', 'Permanent', 'GM'),
(7, 'abdoul aziz', 'Mbodj', 'aziz@esp.mr', 'Permanent', 'GC'),
(8, 'abou', 'deing', 'deing@esp.mr', 'Permanent', 'SID'),
(9, 'aboubecrine', 'med lagdaf', 'aboubecrine@esp.mr', 'Permanent', 'IRT'),
(10, 'ahmed', 'bekar', 'bekar@esp.mr', 'Permanent', 'ST'),
(11, 'ahmed salem', 'Mohamed', 'salem@esp.mr', 'Permanent', 'MPG'),
(12, 'Sidi', 'biha', 'sidibiha@esp.mr', 'Permanent', 'SID'),
(13, 'sidi', 'aly keye', 'keye@esp.mr', 'Permanent', 'GM'),
(14, 'salek', 'sidahmed', 'saleck@esp.mr', 'Permanent', 'GM'),
(15, 'ramadhane', 'nasri', 'ramadhane@esp.mr', 'Permanent', 'GM'),
(16, 'moustaphe', 'elaoun', 'aoun@esp.mr', 'Permanent', 'IRT'),
(17, 'hasseen', 'didi', 'hassen@esp.mr', 'Permanent', 'HE'),
(18, 'MOHAMED', 'sass', 'sass@esp.mr', 'Permanent', 'GE'),
(19, 'mohamed', 'hmeide', 'hmeide@esp.mr', 'Permanent', 'GE'),
(20, 'MOHAMED', 'elfoudhail', 'elfoudhail@esp.mr', 'Permanent', 'MPG'),
(21, 'mohamed', 'cheikh', 'teguedy@esp.mr', 'Permanent', 'GC'),
(22, 'mahmoud', 'seyid', 'seyid@esp.mr', 'Permanent', 'GC'),
(23, 'mahfoud', 'hbib', 'habib@esp.mr', 'Permanent', 'GE'),
(24, 'mabrouk', 'hatira', 'mabrouk@esp.mr', 'Permanent', 'GC'),
(25, 'lemrabot', 'habiboulah', 'habiboulah@esp.mr', 'Permanent', 'GE'),
(26, 'helmi', 'aloui', 'helmi@esp.mr', 'Permanent', 'GE'),
(27, 'elmoktar', 'eby al maaly', 'elmoktar@esp.mr', 'Permanent', 'IRT'),
(28, 'didi', 'magahlah', 'didi@esp.mr', 'Permanent', 'MPG'),
(29, 'dhaou', 'akrout', 'AKROUT@esp.mr', 'Permanent', 'MPG'),
(30, 'daoud', 'blake', 'blake@esp.mr', 'Permanent', 'HE'),
(31, 'choumad', 'mellile naffa', 'naffa@esp.mr', 'Permanent', 'GM'),
(32, 'boudy', 'bilal', 'boudy@esp.mr', 'Permanent', 'GM'),
(33, 'boubacar', 'DAHI', 'DAHI@esp.mr', 'Permanent', 'HE');

-- --------------------------------------------------------

--
-- Structure de la table `enseignement`
--

CREATE TABLE IF NOT EXISTS `enseignement` (
  `id` int(50) NOT NULL AUTO_INCREMENT,
  `nom_em` varchar(50) NOT NULL,
  `nom_E` varchar(50) NOT NULL,
  `type` varchar(40) DEFAULT NULL,
  `plage` varchar(40) NOT NULL,
  `semestre` varchar(40) NOT NULL,
  `duree` int(40) NOT NULL,
  PRIMARY KEY (`id`)
);

--
-- Contenu de la table `enseignement`
--

INSERT INTO `enseignement` (`id`, `nom_em`, `nom_E`, `type`, `plage`, `semestre`, `duree`) VALUES
(1, 'programmation C', 'elhafedh', 'CM', 'P1', 'S2', 90);

-- --------------------------------------------------------

--
-- Structure de la table `id`
--

CREATE TABLE IF NOT EXISTS `id` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
);

-- --------------------------------------------------------

--
-- Structure de la table `plage`
--

CREATE TABLE IF NOT EXISTS `plage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `plage` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
);

--
-- Contenu de la table `plage`
--

INSERT INTO `plage` (`id`, `plage`) VALUES
(1, 'P1'),
(2, 'P2'),
(3, 'P3'),
(4, 'P4'),
(5, 'P5');

-- --------------------------------------------------------

--
-- Structure de la table `semestre`
--

CREATE TABLE IF NOT EXISTS `semestre` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `semestre` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Contenu de la table `semestre`
--

INSERT INTO `semestre` (`id`, `semestre`) VALUES
(1, 'S1'),
(2, 'S2'),
(3, 'S3'),
(4, 'S4'),
(5, 'S5'),
(6, 'S6');

-- --------------------------------------------------------

--
-- Structure de la table `type`
--

CREATE TABLE IF NOT EXISTS `type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(21) NOT NULL,
  PRIMARY KEY (`id`)
);

--
-- Contenu de la table `type`
--

INSERT INTO `type` (`id`, `type`) VALUES
(1, 'CM'),
(2, 'TD'),
(3, 'TP'),
(4, 'PR');

-- --------------------------------------------------------

--
-- Structure de la table `duree`
--

CREATE TABLE IF NOT EXISTS `duree` (
  `duree` int(34) NOT NULL,
  PRIMARY KEY (`duree`)
);
