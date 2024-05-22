 
function ipc(){
  let [interanual_actual, intermensual_actual, meses_actual] = obtenerDatosActual();
  chart = draw_line_chart( intermensual_actual ,interanual_actual ,meses_actual,'chartIpc')
  chartHistorico = draw_line_chart(obtenerDatosInteranualFiltro(),obtenerDatosIntermensualFiltro(),meses_filtro,'chartIpcHistorico')
  chartTabla = draw_line_chart(obtenerDatosInteranualTabla(),obtenerDatosIntermensualTabla(), meses_tabla,'chartTabla')
}

function ipc_division(){
  let [interanual, intermensual, meses] = obtenerDatosDivision();
  chart = draw_line_chart( intermensual ,interanual,meses,'chartDivision')
  
}