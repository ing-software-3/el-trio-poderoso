<?php
// Este archivo funciona como una API (parecido a lo que hace FastAPI)
// Lo que hace es entregar los datos "puros" en formato JSON

include 'conexion.php';

// 1. Busco los productos con poco stock (igual que en el reporte)
$sql = "SELECT nombre, stock, stock_minimo FROM productos WHERE stock <= stock_minimo";
$stmt = $conexion->prepare($sql);
$stmt->execute();
$datos = $stmt->fetchAll(PDO::FETCH_ASSOC);

// 2. Le digo al navegador que esto no es una página web normal, sino una respuesta de datos (JSON)
header('Content-Type: application/json');

// 3. Imprimo los datos para que cualquier otro sistema los pueda leer
// Esto es lo que verías si usaras FastAPI
echo json_encode([
    "titulo" => "Reporte de Stock Bajo",
    "fecha" => date('Y-m-d'),
    "productos_criticos" => $datos
]);
?>