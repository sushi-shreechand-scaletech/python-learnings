import asyncio

# Simulate downloading data from a website
async def download_website(site_name, delay):
    print(f"Starting download from {site_name}...")
    await asyncio.sleep(delay)  # Simulate network delay
    print(f"Finished download from {site_name}")
    return f"Data from {site_name}"

# Main async function to run the tasks
async def main():
    # Create multiple download tasks
    task1 = asyncio.create_task(download_website("Site A", 2))
    task2 = asyncio.create_task(download_website("Site B", 3))
    task3 = asyncio.create_task(download_website("Site C", 1))

    # Wait for all tasks to finish using asyncio.gather
    results = await asyncio.gather(task1, task2, task3)

    # Print the results
    for result in results:
        print(result)

# Run the async main function
asyncio.run(main())
