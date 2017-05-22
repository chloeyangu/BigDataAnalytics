drop table if exists terrorist;
create table terrorist (
  id integer primary key autoincrement,
  success integer not null,
    suicide integer not null,
    targettype integer not null,
    month integer not null,
    region integer not null,
    specificity integer not null,
    attack_type integer not null,
    main_weapon_type integer not null,

);