#' Fetch relevant GitHub repo information from GitHub API
#'
#' Fetch:
#' - main language (based on linguist. Might be inaccurate if people didn't use a
#'   `.gitattributes` file)
#' - license
#' - latest tagged version
#' - presence of a `codemeta.json` file on the default branch
#' - presence of a `CITATION` file on the default branch
#' - presence of a `.zenodo.json` file on the default branch
#'
#' @param owner Owner of the GitHub repository (user or organisation)
#' @param repo Name of the GitHub repository
#'
#' @return A named vector:
#' - `language` (character)
#' - `license` (character)
#' - `version` (character)
#' - `has_codemeta` (logical)
#' - `has_citation` (logical)
#' - `has_zenodo` (logical)
#'
#' @examples
#' fetch_repo_infos("ropensci", "lightr")
#'
#' @importFrom purrr %>%
#'
#' @export
fetch_repo_infos <- function(owner, repo) {

  req <- try(
    gh::gh(
      "/repos/{owner}/{repo}",
      owner = owner,
      repo = repo
    ),
    silent = TRUE
  )

  if (inherits(req, "try-error")) {
    warning(owner, "/", repo, " could not be accessed. Returned a vector of NA")
    return(c(
      language = NA_character_,
      license = NA_character_,
      version = NA_character_,
      has_codemeta = NA_integer_,
      has_citation = NA_integer_,
      has_zenodo = NA_integer_
    ))
  }

  files <- gh::gh(
    "/repos/{owner}/{repo}/git/trees/{branch}",
    owner = owner,
    repo = repo,
    branch = req$default_branch
  )$tree %>%
    purrr::map_chr("path")

  versions <- gh::gh(req$tags_url)

  if (length(versions) == 0) {
    last_version <- NA_character_
  } else {
    last_version <- versions[[1]]$name
  }

  return(c(
    language = req$language,
    license = req$license$spdx_id,
    version = last_version,
    has_codemeta = "codemeta.json" %in% files,
    has_citation = "CITATION" %in% files,
    has_zenodo = ".zenodo.json" %in% files
  ))

}

