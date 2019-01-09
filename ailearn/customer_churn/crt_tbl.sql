﻿create table sample_his(
  service_id										bigint,
  remainder_debt_amt						bigint,
  speech_entry_flg							bigint,
  usim_item_nbr									bigint,
  last_plan_eff_dt							bigint,
  contract_months								bigint,
  avg_replace_cycle							bigint,
  mobile_speech_entry_flg				bigint,
  sui_age												bigint,
  item_months										bigint,
  lcs_cde												bigint,
  tc_1													bigint,
  tc_slope											double,
  tc_nuc												double,
  tc_mdp												double,
  tc_mdn												double,
  ctc_1													bigint,
  ctc_slope											double,
  ctc_nuc												double,
  ctc_mdp												double,
  ctc_mdn												double,
  cfac_1												bigint,
  cfac_slope										double,
  cfac_nuc											double,
  cfac_mdp											double,
  cfac_mdn											double,
  cc_1													bigint,
  cc_slope											double,
  cc_nuc												double,
  cc_mdp												double,
  cc_mdn												double,
  ctac_1												bigint,
  ctac_slope										double,
  ctac_nuc											double,
  ctac_mdp											double,
  ctac_mdn											double,
  mpsc_1												bigint,
  mpsc_slope										double,
  mpsc_nuc											double,
  mpsc_mdp											double,
  mpsc_mdn											double,
  mpc_1													bigint,
  mpc_slope											double,
  mpc_nuc												double,
  mpc_mdp												double,
  mpc_mdn												double,
  msca_1												bigint,
  msca_slope										double,
  msca_nuc											double,
  msca_mdp											double,
  msca_mdn											double,
  kn_1													bigint,
  kn_slope											double,
  kn_nuc												double,
  kn_mdp												double,
  kn_mdn												double,
  ka_1													bigint,
  ka_slope											double,
  ka_nuc												double,
  ka_mdp												double,
  ka_mdn												double,
  churn													bigint
);

create table all_curr like sample_his;