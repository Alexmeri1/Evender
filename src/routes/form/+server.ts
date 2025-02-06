import { json } from '@sveltejs/kit';
import type { RequestHandler } from '@sveltejs/kit';
import { config } from 'dotenv';

import fs from 'fs';
import path from 'path';
import fetch from 'node-fetch';

config();

const API_KEY = process.env.TICKETMASTER_API;
const url = 'https://app.ticketmaster.com/discovery/v2/events.json';

const saveToFile = (data: any, filename = 'user_info.json') => {
	const filePath = path.resolve('./data', filename);
	fs.writeFileSync(filePath, JSON.stringify(data, null, 4));
};

const loadUserData = (filename = 'user_info.json') => {
	const filePath = path.resolve('./data', filename);
	const data = fs.readFileSync(filePath, 'utf-8');
	return JSON.parse(data);
};

export const POST: RequestHandler = async ({ request }) => {
	try {
		const data:{
            location: {
                city:string,
                country:string
            },
            dates: {
                beginning: string,
                end: string
            },
            groupSize: number
        } = await request.json();

		const userCity = data.location.city;
		const userCountry = data.location.country;
		const userBeginDate = `${data.dates.beginning}T00:00:00Z`;
		const userEndDate = `${data.dates.end}T00:00:00Z`;

        console.log(userCity, userCountry, userBeginDate, userEndDate);

		const params = new URLSearchParams(Object.entries({
			apikey: API_KEY,
			city: userCity,
			countryCode: userCountry,
			startDateTime: userBeginDate,
			endDateTime: userEndDate,
			size: '100'
		}).filter(([key, value]) => value !== undefined) as [string, string][]);

        console.log(params)

		const response = await fetch(`${url}?${params}`);
		const events_list: any[] = [];

		if (response.ok) {
			const data: any = await response.json();

            console.log("\n", data)

			if (data._embedded && data._embedded.events) {
				const events = data._embedded.events;

				for (const event of events) {
					const name = event.name || 'No name available';
					const date = event.dates?.start?.localDate || 'No date available';
					const venue = event._embedded?.venues?.[0]?.name || 'No venue available';
					const event_id = event.id || 'No id available';
					const event_url = event.url || 'No URL available';
					const event_info = event.info || 'No information available';

					const price_range = event.priceRanges?.[0] || {};
					const price = (price_range.min + price_range.max) / 2 || 0;

					const event_data = {
						event_name: name,
						date,
						venue,
						price,
						url: event_url,
						info: event_info,
						city: userCity,
						country: userCountry
					};

					events_list.push(event_data);
				}
			} else {
				console.log('No events found.');
			}
		} else {
			console.log(`Failed to fetch data. Status code: ${response.status}`);
			console.log(`Response: ${await response.text()}`);
		}

		return json({ events: events_list });
	} catch (error) {
		console.error('Error processing request:', error);
		return json({ error: 'Failed to process request' }, { status: 500 });
	}
};