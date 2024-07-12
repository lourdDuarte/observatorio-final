function asalariados(){
    let [dif_interanual_filtro, dif_intermensual_filtro,var_interanual_filtro, var_intermensual_filtro, meses_filtro] = obtenerDatosFiltroAsalariado();
    let [dif_interanual, dif_intermensual,var_interanual, var_intermensual, meses] = obtenerDatosAsalariados();

    chartDifActual = draw_line_chart(dif_interanual, dif_intermensual, meses,'Datos - Diferencia','chartDiferenciaActual')
    chartVarActual= draw_line_chart(var_interanual, var_intermensual, meses,'Datos - Variable','chartVariableActual')

    chartDif = draw_line_chart(dif_interanual_filtro, dif_intermensual_filtro, meses_filtro,'Datos - Diferencia','chartDiferencia')
    chartVar = draw_line_chart(var_interanual_filtro, var_intermensual_filtro, meses_filtro,'Datos - Variable','chartVariable')

   
  }
 
  function asalariadosRama(){
    let [var_intertrimestral_filtro, var_cantidad_filtro,meses_rama_filtro] = obtenerDatosFiltroAsalariadoRama();
    chartCantidad = draw_column_chart(var_cantidad_filtro,meses_rama_filtro,'Cantidad registrados', 'chartCantidad' )
    chartIntertrimestral = draw_basic_line_chart(var_intertrimestral_filtro, meses_rama_filtro, 'Variable intertrimestral', 'chartIntertrimestral')
  }