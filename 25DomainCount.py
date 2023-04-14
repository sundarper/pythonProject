import os

# with open('./resources/domain_count.txt', 'r') as user_file:
#     txt_lines = user_file.readlines()
#
#     print(txt_lines)
#     print(type(txt_lines))
#
#     # for lst_content in txt_lines:
#     #     print(lst_content)
#     #     print(type(lst_content))

# ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]

def subDomainCounts(cpdomains):
    counts = {}
    for cpdomain in cpdomains:
        cnt,domain = cpdomain.split()
        print(cnt, domain)
        cnt = int(cnt)
        subdomains = domain.split('.')
        #print("sub domain:", subdomain)

        for j in range(len(subdomains)):
            subdomain = '.'.join(subdomains[j:])
            counts[subdomain] = counts.get(subdomain,0) + cnt
            print("counts", counts, "Counts of Subdomain :", counts[subdomain], " Pre count val :",
                  counts.get(subdomain, 0))
            #print(subdmn, cnts)

    return [str(counts[subdomain])+' '+ subdomain for subdomain in counts]

domain = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]

output = subDomainCounts(domain)
print("Output = ", output)





