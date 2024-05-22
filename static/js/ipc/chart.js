 
function ipc(){
  let [interanual_actual, intermensual_actual, meses_actual] = obtenerDatosActual();
  let [interanual_filtro, intermensual_filtro, meses_filtro] = obtenerDatosFiltro()
  let [interanual_tabla, intermensual_tabla, meses_tabla] = obtenerDatosTabla()
  
  chart = draw_line_chart( intermensual_actual ,interanual_actual ,meses_actual,'chartIpc')
  chartHistorico = draw_line_chart(interanual_filtro, intermensual_filtro, meses_filtro,'chartIpcHistorico')
  chartTabla = draw_line_chart(interanual_tabla, intermensual_tabla, meses_tabla,'chartTabla')
}

function ipc_division(){
  let [interanual, intermensual, meses] = obtenerDatosDivision();
  chart = draw_line_chart( intermensual ,interanual,meses,'chartDivision')
  
}