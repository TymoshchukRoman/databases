Лабораторна робота №2 "Створення додатку бази даних, орієнтованого на взаємодію з СУБД PostgreSQL"
Структура бази даних: 4 таблиці: visitors, gyms, simulators, abonnements. Між сутностями gym та simulator
зв'язок "один до багатьох". Мож сутностями gym та visitor - "багато до багатьох" (для цього була
створена таблиця abonnements).

Команди для роботи з програмою (аргументи вводяться через пробіл):

insertAbonnement   visitor_id gym_id;
insertSimulator    gym_id model weight;
insertGym address  area fee;
insertVisitor      firstname lastname age;
updateLastname     newValue visitor_id;
updateFee newValue gym_id;
generate{Visitors, Gyms, Simulators} number;
delete{Visitor, Gym, Simulator, Abonnement} id;
