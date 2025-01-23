import fs from 'fs';
import { faker } from '@faker-js/faker';

const NUM_ENTRIES = 100;
const FAKE_RATIO = 0.3; // 30% of entries will be fake

function generateJobPost(isFake) {
  const company = faker.company.name();
  const title = faker.person.jobTitle();
  const description = faker.lorem.paragraphs(3);
  
  if (isFake) {
    return {
      company: isFake ? `${company} International` : company,
      title: isFake ? title.toUpperCase() : title,
      description: isFake ? description.toUpperCase() : description,
      salary: isFake ? `$${faker.number.int({ min: 100000, max: 500000 })} - $${faker.number.int({ min: 500001, max: 1000000 })}` : `$${faker.number.int({ min: 30000, max: 150000 })}`,
      location: isFake ? 'REMOTE - ANYWHERE' : faker.location.city(),
      requirements: isFake ? 'NO EXPERIENCE NEEDED!!!' : `${faker.number.int({ min: 1, max: 5 })}+ years of experience`,
      contact_email: isFake ? faker.internet.email({ provider: 'gmail.com' }) : faker.internet.email({ provider: `${company.toLowerCase().replace(/\s/g, '')}.com` }),
      urgency: isFake ? 'IMMEDIATE START!!! LIMITED POSITIONS!!!' : 'Apply by ' + faker.date.future().toLocaleDateString(),
      is_fake: isFake
    };
  } else {
    return {
      company,
      title,
      description,
      salary: `$${faker.number.int({ min: 30000, max: 150000 })}`,
      location: faker.location.city(),
      requirements: `${faker.number.int({ min: 1, max: 5 })}+ years of experience`,
      contact_email: faker.internet.email({ provider: `${company.toLowerCase().replace(/\s/g, '')}.com` }),
      urgency: 'Apply by ' + faker.date.future().toLocaleDateString(),
      is_fake: isFake
    };
  }
}

const jobPosts = [];

for (let i = 0; i < NUM_ENTRIES; i++) {
  const isFake = Math.random() < FAKE_RATIO;
  jobPosts.push(generateJobPost(isFake));
}

const csv = [
  Object.keys(jobPosts[0]).join(','),
  ...jobPosts.map(post => Object.values(post).map(value => `"${value}"`).join(','))
].join('\n');

fs.writeFileSync('job_posts.csv', csv);

console.log('CSV file "job_posts.csv" has been generated with the following sample:');
console.log(csv.split('\n').slice(0, 6).join('\n'));
console.log(`...\nTotal entries: ${NUM_ENTRIES}`);