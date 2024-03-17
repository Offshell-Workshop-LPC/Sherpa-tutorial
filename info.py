import ROOT

fin=ROOT.TFile.Open('sherpa_DYee_MASTER_cff_py_GEN.root') 
event=fin.Get('Events')

print("#event:",event.GetEntries())
event.SetAlias("GenEvent","recoGenParticles_genParticles__GEN.obj")
for ie in range(1):
  event.GetEntry(ie)
  print('Evt ',ie)
  for igen in range(len(event.GenEvent)):
      print('pt:',event.GenEvent[igen].pt(),'pdgid:',event.GenEvent[igen].pdgId(),'Status:',event.GenEvent[igen].status())
