INSERT INTO quartos (numero_quarto)
SELECT generate_series(1, 20)
ON CONFLICT (numero_quarto) DO NOTHING;