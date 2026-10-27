library(readr)
library(dplyr)
library(ggplot2)
library(gridExtra)

result_naive <- read_csv("sol/naive/naive_result.csv")
result_explore_fist <- read_csv("sol/explore_first/explore_first_result.csv")

plot_result <- function(result) {
  solved <- result[!is.na(result$guess_count), ]
  n_solved <- nrow(solved)
  n_failed <- nrow(result[is.na(result$guess_count), ])
  status_df <- data.frame(
    result = c("Solved", "Failed"),
    count = c(n_solved, n_failed)
  )
  status_plot <- ggplot(status_df, aes(x = result, y = count)) +
    geom_bar(stat = "identity") +
    labs(
      title = paste0("Success rate: ", round(n_solved / nrow(result) * 100, 2)),
      x = "",
      y = "Number of words"
    )

  count_df <- solved |>
    group_by(guess_count) |>
    count()
  count_plot <- ggplot(count_df, aes(x = guess_count, y = n)) +
    geom_bar(stat = 'identity') +
    labs(
      title = paste0("Average number of guesses: ", round(mean(solved$guess_count), 2)),
      x = "Number of guesses needed",
      y = "Number of words"
    )
  grid.arrange(status_plot, count_plot, ncol = 2)
}

ggsave("plot_naive.png", plot = plot_result(result_naive))
ggsave("plot_explore_first", plot = plot_result(result_explore_fist))
