{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "d3275789",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "               _                                \n",
       "platform       x86_64-w64-mingw32               \n",
       "arch           x86_64                           \n",
       "os             mingw32                          \n",
       "crt            ucrt                             \n",
       "system         x86_64, mingw32                  \n",
       "status                                          \n",
       "major          4                                \n",
       "minor          2.2                              \n",
       "year           2022                             \n",
       "month          10                               \n",
       "day            31                               \n",
       "svn rev        83211                            \n",
       "language       R                                \n",
       "version.string R version 4.2.2 (2022-10-31 ucrt)\n",
       "nickname       Innocent and Trusting            "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "version"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "019c4577",
   "metadata": {},
   "source": [
    "\n",
    "# Plot 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "3cf8193d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Load the data\n",
    "f.name <- \"household_power_consumption.txt\"\n",
    "f.path <- file.path(\"data\",f.name)\n",
    "\n",
    "data <- read.table(f.path, sep = \";\", header = T, stringsAsFactors = F)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "3ba1879a",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Select the date\n",
    "data$Date <- as.Date(data$Date, format=\"%d/%m/%Y\")\n",
    "selected_dataset <- data[which(data$Date %in% as.Date(c(\"2007-02-01\", \"2007-02-02\"))),]\n",
    "selected_dataset$Global_active_power <- as.numeric(selected_dataset$Global_active_power)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "9a664da9",
   "metadata": {},
   "outputs": [],
   "source": [
    "plot.folder <- \"plot\"\n",
    "if(!file.exists(plot.folder)){dir.create(plot.folder)}\n",
    "\n",
    "path1 <- file.path(plot.folder,\"plot1.png\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "314fb435",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<strong>png:</strong> 2"
      ],
      "text/latex": [
       "\\textbf{png:} 2"
      ],
      "text/markdown": [
       "**png:** 2"
      ],
      "text/plain": [
       "png \n",
       "  2 "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "png(filename=path1, width=480, height = 480)\n",
    "par(las=1)\n",
    "hist(selected_dataset$Global_active_power, xlab = \"Global Active Power (kilowatts)\", \n",
    "     ylab = \"Frequency\", main = \"Global Active Power\", col = \"red\")\n",
    "dev.off()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cfb2761f",
   "metadata": {},
   "source": [
    "## Result PNG\n",
    "\n",
    "![plot1](./plot/plot1.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "feb632dd",
   "metadata": {},
   "source": [
    "# Plot 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "ceda6320",
   "metadata": {},
   "outputs": [],
   "source": [
    "library(lubridate)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "42dad1b8",
   "metadata": {},
   "outputs": [],
   "source": [
    "data <- read.table(f.path, sep = \";\", header = T, stringsAsFactors = F)\n",
    "data$Date <- as.Date(data$Date, format=\"%d/%m/%Y\")\n",
    "data$full_date <- paste0(data$Date, \" \" , data$Time)\n",
    "data$full_date <- as_datetime(data$full_date)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "9baccf88",
   "metadata": {},
   "outputs": [],
   "source": [
    "selected_dataset <- data[which(data$Date %in% as.Date(c(\"2007-02-01\", \"2007-02-02\"))),] \n",
    "selected_dataset$Global_active_power <- as.numeric(selected_dataset$Global_active_power)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "eb127ca0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<strong>png:</strong> 2"
      ],
      "text/latex": [
       "\\textbf{png:} 2"
      ],
      "text/markdown": [
       "**png:** 2"
      ],
      "text/plain": [
       "png \n",
       "  2 "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "path2 <- file.path(plot.folder,\"plot2.png\")\n",
    "png(filename=path2, width=480, height = 480 )\n",
    "with(selected_dataset, plot(Global_active_power~full_date, type='l', \n",
    "                            xlab = \"\", ylab=\"Global Active Power (kilowatts)\" ))\n",
    "dev.off()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7ab528e2",
   "metadata": {},
   "source": [
    "# Result PNG\n",
    "\n",
    "![plot2](./plot/plot2.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3cdf0170",
   "metadata": {},
   "source": [
    "# Plot 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "a1f9eb3c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<strong>png:</strong> 2"
      ],
      "text/latex": [
       "\\textbf{png:} 2"
      ],
      "text/markdown": [
       "**png:** 2"
      ],
      "text/plain": [
       "png \n",
       "  2 "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "## Step1: Reading data\n",
    "data <- read.table(f.path, sep = \";\", header = T, stringsAsFactors = F)\n",
    "\n",
    "\n",
    "## Step2: Create a full day/time column and convert it to POSIXct object\n",
    "data$Date <- as.Date(data$Date, format=\"%d/%m/%Y\")\n",
    "data$full_date <- paste0(data$Date, \" \" , data$Time)\n",
    "data$full_date <- as_datetime(data$full_date)\n",
    "\n",
    "\n",
    "## Step4:Extract data for the following days 2007-02-01, 2007-02-02\n",
    "selected_dataset <- data[which(data$Date %in% as.Date(c(\"2007-02-01\", \"2007-02-02\"))),] \n",
    "\n",
    "\n",
    "\n",
    "## Step5: Change columns with energy submetering to numeric\n",
    "energy_columns <- grepl(\"Sub_metering\", colnames(selected_dataset), fixed=F)\n",
    "selected_dataset[,energy_columns] <- lapply(selected_dataset[,energy_columns], function(x) {as.numeric(x)})\n",
    "\n",
    "\n",
    "path3 <- file.path(plot.folder,\"plot3.png\")\n",
    "\n",
    "## Step6: Plotting line plot - Energy sub metering vs. weekdays\n",
    "png(filename=path3, width=480, height = 480 )\n",
    "\n",
    "\n",
    "with(selected_dataset, plot(Sub_metering_1~full_date, type='l',\n",
    "                            col = \"black\",\n",
    "                            xlab = \"\", ylab=\"Energy sub metering\" ))\n",
    "\n",
    "with(selected_dataset, lines(Sub_metering_2~full_date,\n",
    "                            col = \"red\",\n",
    "                            xlab = \"\", ylab=\"Energy sub metering\" ))\n",
    "\n",
    "\n",
    "with(selected_dataset, lines(Sub_metering_3~full_date,\n",
    "                            col = \"blue\",\n",
    "                            xlab = \"\", ylab=\"Energy sub metering\" ))\n",
    "\n",
    "# adding legend in the right top corner\n",
    "legend(\"topright\", legend=c(colnames(selected_dataset[,energy_columns])), \n",
    "       col= c(\"black\", \"red\", \"blue\"), lwd = 1, cex=0.75)\n",
    "\n",
    "dev.off()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e5611e88",
   "metadata": {},
   "source": [
    "# Result PNG\n",
    "\n",
    "![plot3](./plot/plot3.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1a5e7843",
   "metadata": {},
   "source": [
    "# Plot 4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "796a3382",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<strong>png:</strong> 2"
      ],
      "text/latex": [
       "\\textbf{png:} 2"
      ],
      "text/markdown": [
       "**png:** 2"
      ],
      "text/plain": [
       "png \n",
       "  2 "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "## Step1: Reading data\n",
    "data <- read.table(f.path, sep = \";\", header = T, stringsAsFactors = F)\n",
    "\n",
    "\n",
    "## Step2: Create a full day/time column and convert it to POSIXct object\n",
    "data$Date <- as.Date(data$Date, format=\"%d/%m/%Y\")\n",
    "data$full_date <- paste0(data$Date, \" \" , data$Time)\n",
    "data$full_date <- as_datetime(data$full_date)\n",
    "\n",
    "\n",
    "## Step4:Extract data for the following days 2007-02-01, 2007-02-02\n",
    "selected_dataset <- data[which(data$Date %in% as.Date(c(\"2007-02-01\", \"2007-02-02\"))),] \n",
    "\n",
    "\n",
    "\n",
    "## Step5: Change columns with energy submetering to numeric\n",
    "energy_columns <- grepl(\"Sub_metering\", colnames(selected_dataset), fixed=F)\n",
    "selected_dataset[,energy_columns] <- lapply(selected_dataset[,energy_columns], function(x) {as.numeric(x)})\n",
    "\n",
    "\n",
    "\n",
    "## Step6: Change column \"Global Active Power\", \"Global Rective Power\", \"Voltage\" to numeric\n",
    "power_columns <- grepl(\"Sub_metering\", colnames(selected_dataset), fixed=F)\n",
    "selected_dataset[,power_columns] <- lapply(selected_dataset[,power_columns], function(x) {as.numeric(x)})\n",
    "selected_dataset$Voltage <- as.numeric(selected_dataset$Voltage)\n",
    "\n",
    "\n",
    "## Step7: Plotting\n",
    "path4 <- file.path(plot.folder,\"plot4.png\")\n",
    "png(filename=path4, width=480, height = 480 )\n",
    "\n",
    "# change par to accomodate 4 plots in 2 rows and 2 columns\n",
    "par(mfrow=c(2,2))\n",
    "\n",
    "#1) Global Active power vs. Weekday-Time\n",
    "with(selected_dataset, plot(Global_active_power~full_date, type='l', \n",
    "                            xlab = \"\", ylab=\"Global Active Power (kilowatts)\" ))\n",
    "\n",
    "#2) Voltage vs. Weekday-Time\n",
    "with(selected_dataset, plot(Voltage~full_date, type='l', \n",
    "                            xlab = \"datetime\"))\n",
    "\n",
    "\n",
    "#3) Energy submetering vs. Weekday-time\n",
    "with(selected_dataset, plot(Sub_metering_1~full_date, type='l',\n",
    "                            col = \"black\",\n",
    "                            xlab = \"\", ylab=\"Energy sub metering\" ))\n",
    "\n",
    "with(selected_dataset, lines(Sub_metering_2~full_date,\n",
    "                             col = \"red\",\n",
    "                             xlab = \"\", ylab=\"Energy sub metering\" ))\n",
    "\n",
    "\n",
    "with(selected_dataset, lines(Sub_metering_3~full_date,\n",
    "                             col = \"blue\",\n",
    "                             xlab = \"\", ylab=\"Energy sub metering\" ))\n",
    "\n",
    "# adding legend in the right top corner\n",
    "legend(\"topright\", legend=c(colnames(selected_dataset[,energy_columns])), \n",
    "       bty = \"n\",\n",
    "       col= c(\"black\", \"red\", \"blue\"), lwd = 1, cex=0.8)\n",
    "\n",
    "#4) Global re-ctive power vs. Weekday-Time\n",
    "with(selected_dataset, plot(Global_reactive_power~full_date, type='l', \n",
    "                            xlab = \"datetime\"))\n",
    "\n",
    "\n",
    "\n",
    "dev.off()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bbbd401d",
   "metadata": {},
   "source": [
    "# Result PNG\n",
    "\n",
    "![plot4](./plot/plot4.png)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0ede7271",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "R 4.2.2",
   "language": "R",
   "name": "ir422"
  },
  "language_info": {
   "codemirror_mode": "r",
   "file_extension": ".r",
   "mimetype": "text/x-r-source",
   "name": "R",
   "pygments_lexer": "r",
   "version": "4.2.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
