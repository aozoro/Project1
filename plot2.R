library(lubridate)


f.name <- "household_power_consumption.txt"
f.path <- file.path("data",f.name)
plot.folder <- "plot"
if(!file.exists(plot.folder)){dir.create(plot.folder)}


data <- read.table(f.path, sep = ";", header = T, stringsAsFactors = F)
data$Date <- as.Date(data$Date, format="%d/%m/%Y")
data$full_date <- paste0(data$Date, " " , data$Time)
data$full_date <- as_datetime(data$full_date)

selected_dataset <- data[which(data$Date %in% as.Date(c("2007-02-01", "2007-02-02"))),] 
selected_dataset$Global_active_power <- as.numeric(selected_dataset$Global_active_power)

path2 <- file.path(plot.folder,"plot2.png")
png(filename=path2, width=480, height = 480 )
with(selected_dataset, plot(Global_active_power~full_date, type='l', 
                            xlab = "", ylab="Global Active Power (kilowatts)" ))
dev.off()