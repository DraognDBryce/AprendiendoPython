CREATE DATABASE IF NOT EXISTS master_python;
use master_python;

CREATE TABLE usuarios(
    id          int(25) AUTO_INCREMENT not null,
    nombre      varchar(100),
    apellidos   varchar(255),
    email       varchar(255) not null,
    pasword     varchar(255) not null,
    fecha       date not null,
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    CONSTRAINT uk_email UNIQUE(email)
) ENGINE=InnoDb;

CREATE TABLE notas(
    id          int(25) AUTO_INCREMENT not null,
    usuario_id  int(25) not null,
    titulo      varchar(255) not null,
    contenido MEDIUMTEXT,
    fecha       date not null,
    CONSTRAINT pk_notas PRIMARY KEY,
    CONSTRAINT fk_notas_usuario FOREIGN KEY(usuario_id) REFERENCES usuario(id)


) ENGINE=InnoDb;