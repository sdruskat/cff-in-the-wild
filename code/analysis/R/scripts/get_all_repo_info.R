library(purrr)
pkgload::load_all(".")

repos <- read.csv("../../../data/cff_repositories.csv")

repo_infos <- repos %>%
  dplyr::mutate(infos = purrr::map2(org, name, fetch_repo_infos)) %>%
  tidyr::unnest_wider(infos)

readr::write_csv(repo_infos, "../../../data/repo_infos.csv")
