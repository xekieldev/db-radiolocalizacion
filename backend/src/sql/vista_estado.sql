CREATE VIEW view_file_tracking_status AS
SELECT *, 
    ROW_NUMBER() OVER (PARTITION BY id ORDER BY fecha DESC, hora DESC) AS indice_estado
FROM
(SELECT 
    File.id, 
    File.tipo,
    File.status, 
    File.tramitacion, 
    File.area_asignada,
    file_tracking.envia, 
    file_tracking.recibe, 
    file_tracking.fecha,
    file_tracking.hora, 
    iif(
        file_tracking.recibe = "AGCCTYL" 
        AND (file_tracking.envia = "Buenos Aires"
        OR file_tracking.envia LIKE "%rdoba"
        OR file_tracking.envia = "Salta"
        OR file_tracking.envia = "Comodoro Rivadavia"
        OR file_tracking.envia = "Posadas"
        OR file_tracking.envia = "Lima"
        OR file_tracking.envia LIKE "Neuqu%"), "outbound", 
        iif(
            file_tracking.envia = "AGCCTYL" 
            AND (file_tracking.recibe <> "Buenos Aires"
            AND file_tracking.recibe NOT LIKE "%rdoba"
            AND file_tracking.recibe <> "Salta"
            AND file_tracking.recibe <> "Comodoro Rivadavia"
            AND file_tracking.recibe <> "Posadas"
            AND file_tracking.recibe <> "Lima"
            AND file_tracking.recibe NOT LIKE "Neuqu%"), "finished", "pending")) AS estado

FROM File
INNER JOIN file_tracking ON File.id = file_id
WHERE File.status = 'Available'
)