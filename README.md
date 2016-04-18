# [Kaggle Competiton: Santander Customer Satisfaction](https://www.kaggle.com/c/santander-customer-satisfaction)
Determine an association between the [data](https://www.kaggle.com/c/santander-customer-satisfaction/data) provided by Santander and likelihood of customers leaving.
Deadline: May 2nd.

Resources:
- Data provided is anonymized and originally in Spanish. [Translations and data dictionary discussion here.](https://www.kaggle.com/c/santander-customer-satisfaction/forums/t/19291/data-dictionary)
- [Python code for similar variable grouping](https://www.kaggle.com/walterhan/santander-customer-satisfaction/similar-variable-groupings)

Notes on the variables gleaned from the forums (because no data dictionary or any code book was provided!):
- On the topic of variable meaning/significance: https://www.kaggle.com/cast42/santander-customer-satisfaction/exploring-features/discussion
- On the topic of translation:
  - https://www.kaggle.com/c/santander-customer-satisfaction/forums/t/19291/data-dictionary/110209#post110209
  - imp_ent_varX => importe entidad => amount for the bank office
  - imp_op_varX_comer => importe opcion comercial => amount for commercial option
  - imp_sal_varX => importe salario => amount for wage
  - ind_varX_corto => indicador corto => short (time lapse?) indicator/dummy
  - ind_varX_medio => indicador medio => medium-sized (time lapse?) indicator/dummy
  - ind_varX_largo => indicador largo => long-sized (time lapse?) indicator/dummy
  - sald_varX => saldo => balance
  - delta_imp_amort_varX_1y3 => importe amortización 1 y 3 => amount/price for redemption (?) 1 and 3
  - delta_imp_aport_varX_1y3 => importe aportación 1 y 3 => amount/price for contribution (?) 1 and 3
  - delta_imp_reemb_varX_1y3 => importe reembolso 1 y 3 => amount/price for refund 1 and 3
  - delta_imp_trasp_varX_out_1y3 => importe traspaso 1 y 3 => amount/price for transfer 1 and 3
  - imp_venta_varX => importe venta => sale fee.
  - ind_varX_emit_ult1 => indicador emitido => indicator of emission
  - ind_varX_recib_ult1 => indicador recibido => indicator of reception
  - num_varX_hace2 => número hace 2 => number [of variable X ] done two units in the past
  - num_med_varX => número medio => mean number [of variable X]
  - num_meses_varX => número de meses => number of months [for variable X]
  - saldo_medio_varX => saldo medio => average balance
  - delta_imp_venta_varX_1y3 = > importe de venta 1 y 3 => fee on sales [for variable X] 1 and 3
  - As you see, some make sense and some not. Most variables end with "_ultX", which does not make much sense to me (from "últimaX" -- "lastX"?).
- 'Indicator' variables seem to come in pairs often (not all the time).
  - https://www.kaggle.com/c/santander-customer-satisfaction/forums/t/19291/data-dictionary/110586#post110586
  - "my hypothesis has been that ind_XXX indicates whether a person has chosen this banking product (and 0 therefore means that he has not chosen it), whereas ind_XXX_0 indicates that the customer has explicitly opted out of the product. Note that when ind_XXX_0 is 1, the rest of the variables in the group are zeros."
  - "W/ regards to ind_varX and ind_varX_0, take a look at the relationship w/ those 2 to num_varX and num_varX_0 - looking at those grouped together for the same var (i.e. var33 for example) should give a rough picture on what they represent in terms of products and customer offerings"
- 'var15' likely represents age (in Chile?).
  - https://www.kaggle.com/c/santander-customer-satisfaction/forums/t/19291/data-dictionary/110414#post110414
  - "And if I recall correctly, there was a huge campaign several years ago from Santander targeted at university students (in some cases it was almost mandatory opening an account with them if you wanted to access to some university services, go figure...), which would explain the spike that this variable has between 20-25."
- var13, saldo_var13 = saldo_var13_corto + saldo_var13_largo
  - var13 balance = var13 balance short + var13 balance long
- "After removing redundant features (i.e., constant or duplicate) the data has 306 features, which breakdown to 43 floats, 263 Ints, and 0 Strings (https://www.kaggle.com/c/santander-customer-satisfaction/forums/t/19291/data-dictionary/110947#post110947)
  - Int feature var3 has a minimum of -999999, which which appears to be an error code
  - 18 Integer features have a max of 9999999999, which appears to be an error code
  - Features like
    - "ind_" are boolean (i.e., 0 or 1)
    - "num_" are mostly ranges like 3, 6, 9, 12, ... for example, var42 number 0 -> [0 - 18, 114]. I'm guessing these are month. Since most are in steps of three, this would be quarters."
