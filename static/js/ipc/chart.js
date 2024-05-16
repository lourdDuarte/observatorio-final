 
function ipc(){
  chart = draw_line_chart(obtenerDatosInteranualActual(),obtenerDatosIntermensualActual(),meses,'chartIpc')
  chartHistorico = draw_line_chart(obtenerDatosInteranualFiltro(),obtenerDatosIntermensualFiltro(),meses_filtro,'chartIpcHistorico')
}