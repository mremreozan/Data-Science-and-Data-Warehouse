package com.google.cloud.training.dataanalyst.javahelp;

import java.util.Arrays;

import org.apache.beam.sdk.Pipeline;
import org.apache.beam.sdk.io.TextIO;
import org.apache.beam.sdk.transforms.Count;
import org.apache.beam.sdk.transforms.FlatMapElements;
import org.apache.beam.sdk.transforms.MapElements;
import org.apache.beam.sdk.values.KV;
import org.apache.beam.sdk.values.PCollection;
import org.apache.beam.sdk.values.TypeDescriptors;

public class BeamBatchPipeline {
    public static void main(String[] args) {
        Pipeline pipeline = Pipeline.create();

        String input = "gs://qwiklabs-gcp-01-4db873b7cba6/reviews.csv";
        String output = "gs://qwiklabs-gcp-01-4db873b7cba6/output";

        // Step 1 - Read CSV file.
        PCollection<String> csvRows = pipeline.apply("Read from CSV",
                TextIO.read().from(input));

        // Step 2 - Extract ratings and count them.
        PCollection<KV<String, Long>> ratingsCounts = csvRows
                .apply("Extract Ratings",
                        FlatMapElements.into(TypeDescriptors.strings())
                                .via(csvRow -> Arrays.asList(csvRow.split(",")[1])))
                .apply("Count Ratings", Count.<String>perElement());

        // Step 3 - Write results to CSV
        ratingsCounts
                .apply("FormatResults", MapElements.into(TypeDescriptors.strings())
                        .via((KV<String, Long> ratingsCount) -> ratingsCount.getKey() + " " + ratingsCount.getValue()))
                .apply(TextIO.write().to(output).withSuffix(".csv"));

        // Run the pipeline and wait till it finishes before exiting
        pipeline.run().waitUntilFinish();
    }
}