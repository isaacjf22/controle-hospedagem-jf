TRUNCATE gastos, hospedagens, clientes, funcionarios RESTART IDENTITY CASCADE;
UPDATE quartos SET status = 'LIVRE';