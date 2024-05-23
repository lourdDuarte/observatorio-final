function asalariados(){
    let [dif_interanual_filtro, dif_intermensual_filtro,var_interanual_filtro, var_intermensual_filtro, meses_filtro] = obtenerDatosFiltroAsalariado();

    // let [interanual_filtro, intermensual_filtro, meses_filtro] = obtenerDatosFiltro()
    // let [interanual_tabla, intermensual_tabla, meses_tabla] = obtenerDatosTabla()
    
    chartDif = draw_line_chart(dif_interanual_filtro, dif_intermensual_filtro, meses_filtro,'Datos - Diferencia','chartDiferencia')
    chartVar = draw_line_chart(var_interanual_filtro, var_intermensual_filtro, meses_filtro,'Datos - Variable','chartVariable')

   
  }