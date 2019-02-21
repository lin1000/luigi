#!/bin/bash

in=${1}
out=${2}

echo "id,name,urlname,link,rating,created,description,organiserName,organiserMemberId" > ${out}
jq -r '.[] | [.id, .name, .urlname, .link, .rating, .created, .description, .organizer.name, .organizer.member_id] | @csv' ${in} >> ${out}