def lista(matrizX, matrizY):
 


  resultX = 0
  resultY = 0
  result_mult = 0

  for linhaX in matrizX:
    for colunaX in linhaX:
      resultX = colunaX + resultX

  for linhaY in matrizY:
    for colunaY in linhaY:
      resultY = colunaY + resultY

  print('imprime primeiro resultado', resultX)
  print('imprime segundo resultaddo', resultY)

  result_mult =  resultX * resultY

  print('imprime mult', result_mult)
  
matrizX = [[1,2,3],[1,2,3]]
matrizY = [[1,2,3],[10,20,30]]

lista(matrizX, matrizY)
