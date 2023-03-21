#Load the data
f.name <- "household_power_consumption.txt"
f.path <- file.path("data",f.name)

data <- read.table(f.path, sep = ";", header = T, stringsAsFactors = F)


#Select the date
data$Date <- as.Date(data$Date, format="%d/%m/%Y")
selected_dataset <- data[which(data$Date %in% as.Date(c("2007-02-01", "2007-02-02"))),]
selected_dataset$Global_active_power <- as.numeric(selected_dataset$Global_active_power)

plot.folder <- "plot"
if(!file.exists(plot.folder)){dir.create(plot.folder)}

path1 <- file.path(plot.folder,"plot1.png")

png(filename=path1, width=480, height = 480)
par(las=1)
hist(selected_dataset$Global_active_power, xlab = "Global Active Power (kilowatts)", 
     ylab = "Frequency", main = "Global Active Power", col = "red")
dev.off()